class paramethod{
int height,length,width;

void setvalue(int h,int l, int w)
{
height=h;
length=l;
width=w;
}
int showvolume()
{
return height*length*width;
}
public static void main(String[] args)
{
paramethod v1=new paramethod();
paramethod v2=new paramethod();
v1.setvalue(5,10,15);
v2.setvalue(10,20,30);

int v=v1.showvolume();
System.out.println("Volume of box 1 is "+v);
v=v2.showvolume();
System.out.println("Volume of box 2 is "+v);
}
}

