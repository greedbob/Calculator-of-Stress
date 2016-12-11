
p=a*b;
pn=p*p';
ans1=a(1)*b(1)^2 + a(5)*b(2)^2 + a(9)*b(3)^2 + 2a(2)*b(1)*b(2) + 2a(3)*b(2)*b(3) + 2a(6)*b(1)*b(3);
ans2=(pn^2-ans1^2)^0.5;
%% left=[cos(a),sin(a);-sin(a),cos(a)];
% x=left*b*(left');
% disp(x);
