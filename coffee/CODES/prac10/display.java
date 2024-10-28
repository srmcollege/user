import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
public class display extends HttpServlet {
@Override
public void service(ServletRequest req,ServletResponse res)
        throws ServletException,IOException{
PrintWriter pw=res.getWriter();
res.setContentType("text/html");
try{
    Class.forName("oracle.jdbc.driver.OracleDriver");
    pw.println("Driver loaded successfully...");
}catch(ClassNotFoundException ex) {
    pw.println("Exception found is...."+ex);
}
try{
  Connection con=DriverManager.getConnection(
          "jdbc:oracle:thin:@localhost:1521:XE",
          "system","manager");
    pw.println("<br>Connection made successfully...");
    Statement stmt=con.createStatement();
    ResultSet rs=stmt.executeQuery("select*from student");
    
    pw.println("<table border=1>");
    pw.println("<tr>");
    pw.println("<th>ID</th>");
    pw.println("<th>Name</th>");
    pw.println("<th>ADDRESS</th>");
    pw.println("</tr>");
    
    while(rs.next()){
        pw.println("<tr>");
        pw.println("<td>"+rs.getInt(1)+"</td>");
        pw.println("<td>"+rs.getString(2)+"</td>");
        pw.println("<td>"+rs.getString(3)+"</td>");
        pw.println("</tr>");
    }
}catch(SQLException e){
    pw.println("Exception found is...."+e);
}
}
}