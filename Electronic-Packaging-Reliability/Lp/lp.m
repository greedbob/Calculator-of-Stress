function []=lp(p)
N=1000;
n=30;
d=3;
lp=[];
sum_lp=0;
for i=0:1:d
    lp(i+1)=nchoosek(N*p,i)*nchoosek(N-N*p,n-i)/nchoosek(N,n);
    %disp(lp(i+1));
    sum_lp=sum_lp+lp(i+1);
end
disp(sum_lp);
