import java.sql.*;

class jdbcdisplay{
public static void main(String args[]){
try{
Class.forName("oracle.jdbc.driver.OracleDriver");
System.out.println("Driver loaded successfully...");

Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","system","manager");
System.out.println("Connection made successfully...");

Statement stmt=con.createStatement();

ResultSet rs=stmt.executeQuery("select*from student where id=3");

System.out.println("ID	Name	Address		");
while(rs.next())
{
System.out.println(""+rs.getInt(1)+"	"+rs.getString("name")+"	"+rs.getString(3));
}
}catch(Exception e)
{
System.out.println("Exception found is..."+e);
}
}
}

