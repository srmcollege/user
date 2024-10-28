class v1{
int a;
}
class v2 extends v1{
int a;

v2(int x,int y){
a=x;
super.a=y;
}

void show()
{
System.out.println("Value of a of subclass is "+a);
System.out.println("Value of a of superclass is "+super.a);
}
}

class varoverriding{
public static void main(String[] args){
v2 x=new v2(10,20);
x.show();
}
}

