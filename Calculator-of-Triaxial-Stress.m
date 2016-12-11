function fun(   )

syms n1 n2 n3 x y z t1 t2 t3 real;

 n=[n1,n2,n3]';
 A=[x,t1,t2;t1,y,t3;t2,t3,z];
 
%给定方向应力状态符号运算
 
 n=n/(n(1)^2+n(2)^2+n(3)^2)^0.5;
 p=A*n;
 xx=p'*n;
 tt=(p'*p-xx^2)^0.5;

 AA=input('三向应力状态');

%主应力计算

syms b real;
 B=A-[b,0,0;0,b,0;0,0,b];
 bb=det(B)==0;
 bbb=subs(bb,{x,y,z,t1,t2,t3},{AA(1),AA(5),AA(9),AA(2),AA(3),AA(6)});
 ss=solve(bbb);
 ss=eval(ss)
 

 disp('主应力');