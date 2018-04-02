function []=LL()
% 初始数据
N=25;
T=500;
t0=[0.005 0.1 0.2 1.0 1.0 2.3 9.3 10.1 14.2 16.4 29.7 155.2 172.6 393.1 442.8 445.0];
[m,n]=size(t0);

% 最小二乘法求参数
Ft=1/25*[1:1:16];
a=log(t0);
b=log(log(1./(1-Ft)));


x2=sum(a.^2);
x1=sum(a);
x1y1=sum(a.*b);
y1=sum(b);

k=(n*x1y1-x1*y1)/(n*x2-x1*x1);
j=(y1-k*x1)/n;

disp(k);
disp(j);

hold on;
x=[-8:0.01:8];
plot(a,b,'x');
plot(x,k*x+j);

t=[0:0.000001:2];
F=1-exp(-t.^k./exp(-j));
F25=1-exp(-(t+25).^k./exp(-j));

r=F*N;
rr=F25*N-r;
cost=50*t*N+350*r+1200*rr;
mix_where=find(cost==min(cost));

disp(mix_where);
disp(min(cost));
hold on;
plot(t,cost);
plot(mix_where*0.000001,min(cost),'r*');
text(mix_where*0.000001,min(cost),'  (0.610487,8617.8)');