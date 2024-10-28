class mysubinterface implements myinterface{
int c;

public void show() {
System.out.println("Inside overridden show()");
}
public int add(int x,int y){
return x+y;
}
void display(){
c=a+b;
System.out.println("Addition is " + c);
}
}

public class main
{
public static void main(String[] args)
{
mysubinterface m =new mysubinterface();
m.show();
m.display();
int x=m.add(10,20);
System.out.println("Addition is "+x);
}
}
