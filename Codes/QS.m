subplot(2,1,1);
cursec1 = colR(7.119e5:7.125e5);
cursec2 = colS(7.119e5:7.125e5);
plot([7.119e5:7.125e5],cursec1,'o');
title('引风机3B润滑油进油管油温');
subplot(2,1,2);
plot([7.119e5:7.125e5],cursec2,'o');
title('引风机3B电机轴承润滑油回油管油温');
print -dpng 6.png