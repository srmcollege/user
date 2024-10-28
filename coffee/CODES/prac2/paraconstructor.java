class paraconstructor{
int height,length,width;
paraconstructor(int h,int l,int w)
{
height=h;
length=l;
width=w;
}
int calvolume()
{
return height*length*width;
}
public static void main(String[] args)
{
paraconstructor d1=new paraconstructor(50,60,70);
paraconstructor d2=new paraconstructor(80,90,100);

int volume;
volume=d1.calvolume();
System.out.println("Volume of box 1 is "+volume);
volume=d2.calvolume();
System.out.println("Volume of box 2 is "+volume);
}
}

