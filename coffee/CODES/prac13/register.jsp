<%@page import="java.sql.*" contentType="text/html" 
        pageEncoding="UTF-8"%>
<html>
<body>
<%
int rollno=Integer.parseInt(request.getParameter("rollno"));
String name=request.getParameter("name");
String address=request.getParameter("address");
try{
Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con=DriverManager.getConnection(
        "jdbc:oracle:thin:@localhost:1521:XE","system","manager");
Statement stmt=con.createStatement();
stmt.executeUpdate("insert into student values("
        +""+rollno+",'"+name+"','"+address+"')");             
out.println("Record inserted");
}catch(Exception e){
out.println("Exception found..."+e);             
}
%>
</body>
</html>

