import java.sql.*;

class jdbcdemo{
public static void main(String args[]){
try{
Class.forName("oracle.jdbc.driver.OracleDriver");
System.out.println("Driver loaded successfully...");

Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","system","manager");
System.out.println("Connection made successfully...");
System.out.println("");
Statement stmt=con.createStatement();
stmt.executeUpdate("insert into student values(1,'Sanjar','Malvan')");
System.out.println("Record inserted successfully...");

ResultSet rs=stmt.executeQuery("select*from student");

System.out.println("ID	Name	Address		");
while(rs.next())
{
System.out.println(""+rs.getInt(1)+"	"+rs.getString("name")+"	"+rs.getString(3));
}

stmt.executeUpdate("update student set address='Malvan' where id=5");
System.out.println("Record updated successfully");

ResultSet rst=stmt.executeQuery("select*from student");

System.out.println("ID	Name	Address		");
while(rst.next())
{
System.out.println(""+rst.getInt(1)+"	"+rst.getString("name")+"	"+rst.getString(3));
}

stmt.executeUpdate("delete from student where id=3");
System.out.println("Record deleted successfully");

ResultSet res=stmt.executeQuery("select*from student");

System.out.println("ID	Name	Address		");
while(res.next())
{
System.out.println(""+res.getInt(1)+"	"+res.getString("name")+"	"+res.getString(3));
}

}catch(Exception e)
{
System.out.println("Exception found is..."+e);
}
}
}
