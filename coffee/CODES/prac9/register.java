import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
public class register extends HttpServlet{
@Override
public void service(ServletRequest req,ServletResponse res)
        throws ServletException,IOException{
PrintWriter pw=res.getWriter();
res.setContentType("text/html");
try{
    Class.forName("oracle.jdbc.driver.OracleDriver");
}catch(ClassNotFoundException ex) {
    pw.println("Exception found is...."+ex);
}
try{
  Connection con=DriverManager.getConnection(
          "jdbc:oracle:thin:@localhost:1521:XE",
          "system","manager");
    PreparedStatement pstmt;
    
    int rollno=Integer.parseInt(req.getParameter("rollno"));
    String name=req.getParameter("name");
    String address=req.getParameter("address");
    String phone=req.getParameter("phone");
    
    String insert="insert into users values(?,?,?,?)"; 
    pstmt=con.prepareStatement(insert);
    pstmt.setInt(1,rollno);
    pstmt.setString(2,name);
    pstmt.setString(3,address);
    pstmt.setString(4,phone);
    
    int rows=pstmt.executeUpdate();
    if(rows>0){
        pw.println("<h2>Registration Successful</h2>");
    }else{
        pw.println("<h2>Registration Failed. Try Again.</h2>");
        }
}catch(SQLException e){
    pw.println("Exception found is...."+e);
}
}
}

