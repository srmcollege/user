class constructor{
int height,length,width;
constructor()
{
height=10;
length=20;
width=30;
}
int calvolume()
{
return height*length*width;
}
public static void main(String[] args)
{
constructor d1=new constructor();
constructor d2=new constructor();

int volume;
volume=d1.calvolume();
System.out.println("Volume of box 1 is "+volume);
volume=d2.calvolume();
System.out.println("Volume of box 2 is "+volume);
}
}

