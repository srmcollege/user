class volume{
int height,length,width;

void showvolume()
{
System.out.println("Volume of box is "+height*length*width);
}
public static void main(String[] args)
{
volume v1=new volume();
volume v2=new volume();
v1.height=5;
v1.length=10;
v1.width=15;

v2.height=10;
v2.length=20;
v2.width=30;
v1.showvolume();
v2.showvolume();
}
}

