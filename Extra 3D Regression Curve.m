#see extra figure 4 for plotting the 3d regression curve
clc



#load the training dataset
data=load('MergeSort.txt');
#or
#data=load('QuickSortLastPivot.txt');

[row,col]=size(data)
#extract first column as y practical running time
y=data(:,1);
#and subsequent rows as x the features n
x=data(:,2:end)
size(x)


#extend the features to get a regression fit such as nlogn,n,etc

#for QuickSort
#x = [x,x.*x]
#for MergeSort/QuickSort
x = [x,x.*log2(x)]



[row,col]=size(x)

#plotting_data_2d
figure(1)
plot(x(:,1), y, 'rx', 'MarkerSize', 10) #try experimenting with -xr -ob
title('Plot for Algorithm MergeSort');
#title('Plot for Algorithm QuickSort');
ylabel('Time Complexity u(n)'); % Set the y  axis label
xlabel('Input Size n'); % Set the x  axis label
legend('label1','label2')
#plotting data 3d if 3 (or more) variables are present
if(col>=2)
  figure(2)
  scatter3(x(:,1),x(:,2),y)
  title('Plot for Algorithm MergeSort');
  #title('Plot for Algorithm QuickSort');
  xlabel('Feature1 n1=n'); % Set the x  axis label
  ylabel('Feature2 n2=nlogn'); % Set the y  axis label
  zlabel('u(n)'); % Set the z axis label
endif



%% ================ Gradient Descent/Optimization ================


m = length(y);
#no of training examples
x = [ones(m , 1) , x];
% Add intercept term to X
[row,col]=size(x)
theta_0 = [zeros(1,col)]'
#initial theta is just a column vector of the number of features in x

options = optimset('GradObj' , 'on' , 'MaxIter' , 1500);
[theta_opt, cost] = fminunc(@ (t) computeCost(x,y,t) , theta_0 , options) 

#plotting the results/regression line obtained

figure(3)
plot(x(:,2), y, 'rx', 'MarkerSize', 10) #-xr -ob

title('Plot for Algorithm MergeSort');
#title('Plot for Algorithm QuickSort');
ylabel('Time Complexity u(n)'); % Set the y ? axis label
xlabel('Input Size n'); % Set the x ? axis label
#print first column only
hold on;
#now plotting the regression line
h=theta_opt'*x';
plot(x(:,2), h)
legend('original data points','regression line')
hold off;


figure(4)
scatter3(x(:,2),x(:,3),y)
title('Plot for Algorithm MergeSort');
#title('Plot for Algorithm QuickSort');
xlabel('Feature1 n1=n'); % Set the x  axis label
ylabel('Feature2 n2=nlogn'); % Set the y  axis label
zlabel('u(n)'); % Set the z axis label
hold on;
t=x(:,2);
#t=t';#row
h=t;
t = [ones(size(t)),t,t.*log2(t)];
size(t);
l=t*theta_opt;
size(l);
y=h.*log2(h);
plot3(h,y,l,'linewidth',3)
legend('original data points','regression line')
hold off;

