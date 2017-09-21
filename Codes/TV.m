colt = matrix(:,19);
colu = matrix(:,20);
colv = matrix(:,21);
figure
subplot(3,1,1);
plot(colt);
title('引风机3B油箱油温2');
subplot(3,1,2);
plot(colu,'-');
title('引风机3B油箱油温2高');
subplot(3,1,3);
plot(colv,'-');
title('引风机3B油箱油温2低')
print -dpng 7.png

figure
subplot(2,1,1);
cursec1 = colt(2.25e5:2.255e5);
plot([2.25e5:2.255e5],cursec1,'o');
title('引风机3B油箱油温2');

subplot(2,1,2);
cursec2 = colv(2.25e5:2.255e5);
plot([2.25e5:2.255e5],cursec2,'o');
title('引风机3B油箱油温2低')
print -dpng 8.png

figure

subplot(2,1,1);
cursec3 = colt(8e5:8.003e5);
plot([8e5:8.003e5],cursec3,'o');
title('引风机3B油箱油温2');

subplot(2,1,2);
cursec4 = colu(8e5:8.003e5);
plot([8e5:8.003e5],cursec4,'o');
title('引风机3B油箱油温2高');
print -dpng 9.png

figure
subplot(2,1,1);
cursec3 = colt(8e5:8.003e5);
plot([8e5:8.003e5],cursec3,'o');
title('引风机3B油箱油温2');
subplot(2,1,2);
cursec5 = colv(8e5:8.003e5);
plot([8e5:8.003e5],cursec5,'o');
title('引风机3B油箱油温2低');
print -dpng 11.png

figure
cursec6 = colt(9e5:9.01e5);
plot([9e5:9.01e5],cursec6,'-');
title('引风机3B油箱油温2');
print -dpng 12.png