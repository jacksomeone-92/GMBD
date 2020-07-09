# Forecasting Time Series Session 4 Exercise


#load packages
install.packages("readr")
library(readr)
install.packages("data.table")
library(data.table)
install.packages("fBasics")
library(fBasics)
install.packages("forecast")
library(forecast)
library(ggplot2)


#read data

folder_path <- "C:/Users/nicolas-greull/Documents/Privat/IE/Term 2/Time Series/"
data <- fread(file.path(folder_path, "Session4sim.csv"))

head(data)

series2 <- as.data.frame(data$Serie2)

#series2_new <- as.data.frame(data$Serie2)
#series2_new <- series2_new[-c(201:2000), ]


#adding series column
series2$continuous <- c(1:200)

#removing rows 201:2000 as they are empty for this series
series2 <- series2[-c(201:2000), ]

head(series2)
summary(series2)

# achieving stationarity and identifying the model
# Is my data stationary? Do I have to take any differences or logs?

par(mar=c(2,2,2,2))

ts.plot(series2)  

par(mfrow=c(2,1))
acf(series2)  
pacf(series2)

ndiffs(y, alpha=0.05, test=c("adf"))

# estimating the model
fit<-arima(series2,order=c(0,0,0))    # do we need an AR(p)? Are the residuals WN?
fit # we find the information about the estimated parameters

par(mfrow=c(3,1))
ts.plot(fit$residuals)
acf(fit$residuals)
pacf(fit$residuals)    

Box.test(fit$residuals,lag=20)
# already white noise?
# Do we need a non-linear model (quadratic)?

par(mfrow=c(3,1))
ts.plot(fit$residuals^2)
acf(fit$residuals^2)
pacf(fit$residuals^2)    

Box.test(fit$residuals^2,lag=10)

# testing for normality 
shapiro.test(fit$residuals)  # 95% confidence intervals are robust for any kind of distribution

hist(fit$residuals,prob=T,ylim=c(0,0.25),xlim=c(mean(fit$residuals)-3*sd(fit$residuals),mean(fit$residuals)+3*sd(fit$residuals)),col="red")
lines(density(fit$residuals),lwd=2)
mu<-mean(fit$residuals)
sigma<-sd(fit$residuals)
x<-seq(mu-3*sigma,mu+3*sigma,length=100)
yy<-dnorm(x,mu,sigma)
lines(x,yy,lwd=2,col="blue")


# Forecasting
y.pred<-predict(fit,n.ahead=6)
y.pred$pred # point predictions
y.pred$se  # standard error for the point predictions to compute confidence intervals

ts.plot(y)
lines(y.pred$pred,col="red")
lines(y.pred$pred+1.96*y.pred$se,col="red",lty=3)
lines(y.pred$pred-1.96*y.pred$se,col="red",lty=3)

# Comparing the real values with the predicted ones
real<-datos[,2][91:96] 
c=1:6
plot(c,real,type="b",col="red")
lines(c,y.pred$pred,col="blue",type="b")
legend("bottomleft",c("real","forecast"),
       col = c("red","blue"),pch = c(1,1),bty ="n" )



# quantiles of a normal distribution
xxx<-rnorm(20000)  
quantile(xxx,c(0.025,0.05,0.10,0.90,0.95,0.975)) # percentiles
quantile(fit$residuals,c(0.025,0.05,0.10,0.90,0.95,0.975)) # percentiles

# computing quantiles to the residual distribution

quantile(fit$residuals, probs=c(0.025,0.975)) # 95% confidence interval
-1.96*sd(fit$residuals)

quantile(fit$residuals, probs=c(0.1,0.9)) # 80% confidence interval
-1.28*sd(fit$residuals)

quantile(fit$residuals, probs=c(0.2,0.8)) # 60% confidence interval
-0.84*sd(fit$residuals)