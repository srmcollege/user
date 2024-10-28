class loop{
public static void main(String[] args){
System.out.println("For loop...");
for(int i=1;i<=10;i++)
{
System.out.println("Current value of i is "+i);
}
System.out.println("Loop terminated...");
System.out.println("While loop");
int i=1;
while(i<=10){
System.out.println("Current value is "+i);
i++;
}
System.out.println("Loop terminated....");
System.out.println("Do while loop...");
do{
System.out.println("Current value is "+i);
i++;
}
while(i<=10);
System.out.println("Loop terminated....");
}
}