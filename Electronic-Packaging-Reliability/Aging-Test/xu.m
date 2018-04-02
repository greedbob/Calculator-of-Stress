function []=xu()
t=0:0.01:5;
f1=1-exp(-t.^0.2431/5.2593);
f2=1-exp(-(t+25).^0.2431/5.2593);
w=1200*f2-850*f1+50*t;
x=find(w==min(w));
disp(x);
plot(t,w);