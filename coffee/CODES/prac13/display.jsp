<%@page import="java.sql.*" contentType="text/html"
        pageEncoding="UTF-8"%>
<html>
<body>
<%
try{
Class.forName("oracle.jdbc.driver.OracleDriver");
}catch(ClassNotFoundException ex){
}
try{
Connection con=DriverManager.getConnection(
"jdbc:oracle:thin:@localhost:1521:XE",
"system","manager");
Statement stmt=con.createStatement();
ResultSet rs=stmt.executeQuery("select*from student");

out.println("<table border=1>");
out.println("<tr>");
out.println("<th>Roll No</th>");
out.println("<th>Name</th>");
out.println("<th>ADDRESS</th>");
out.println("</tr>");

while(rs.next()){
out.println("<tr>");
out.println("<td>"+rs.getInt(1)+"</td>");
out.println("<td>"+rs.getString(2)+"</td>");
out.println("<td>"+rs.getString(3)+"</td>");
out.println("</tr>");
}
}catch(SQLException e){
out.println("Exception found is...."+e);
}
%>
</body>
</html>



