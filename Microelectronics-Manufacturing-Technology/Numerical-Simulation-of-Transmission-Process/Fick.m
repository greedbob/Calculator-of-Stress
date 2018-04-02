function []=Fick()
% IN=input('输入参数');
hold on;
Cb = 10;
Cs = 10^15;

t1 = 1000;
DT = 1/1000000^2*[0.1^2,0.2^2,0.4^2];
z = 0:10^(-9):2*10^(-6);

C1 = Cs*erfc(z/(2*sqrt(DT(1))));
C2 = Cs*erfc(z/(2*sqrt(DT(2))));
C3 = Cs*erfc(z/(2*sqrt(DT(3))));
Qt1 = 2/sqrt(pi)*Cs*sqrt(DT(1));
Qt2 = 2/sqrt(pi)*Cs*sqrt(DT(2));
Qt3 = 2/sqrt(pi)*Cs*sqrt(DT(3));

plot(z,C1);
plot(z,C2);
plot(z,C3);
% semilogy(z,C1);
% semilogy(z,C2);
% semilogy(z,C3);

% C1= 0:0.000001:0.1;
% set(gca, 'XLim',[0,1]);
% set(gca, 'YLim',[0,1]);

CC1=Qt2/sqrt(pi*DT(1))*exp(-z.^2/(4*DT(1)));
CC2=Qt2/sqrt(pi*DT(2))*exp(-z.^2/(4*DT(2)));
CC3=Qt2/sqrt(pi*DT(3))*exp(-z.^2/(4*DT(3)));

plot(z,CC1);
plot(z,CC2);
plot(z,CC3);

Qt = [Qt1,Qt2,Qt3];
disp(Qt);

x(1) = sqrt(4*DT(1)*log(Qt2/(Cb*sqrt(pi*DT(1)))));
x(2) = sqrt(4*DT(2)*log(Qt2/(Cb*sqrt(pi*DT(2)))));
x(3) = sqrt(4*DT(3)*log(Qt2/(Cb*sqrt(pi*DT(3)))));
disp(x);