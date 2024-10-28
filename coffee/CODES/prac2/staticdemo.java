class staticdemo{
static int a=5;
static int b;
static int c=500;

static{
b=a*10;
}
static void show(int x)
{
System.out.println("Value of a is "+a);
System.out.println("Value of b is "+b);
System.out.println("Value of c is "+c);
System.out.println("Value of x is "+x);
}
public static void main(String[] args){
show(1000);

System.out.println("Value of a is "+a);
staticdemo c1=new staticdemo();
staticdemo c2=new staticdemo();
c1.c=500;
c2.c=1;
System.out.println("Value of c is "+c1.c);
System.out.println("Value of c is "+c2.c);
} 
}

