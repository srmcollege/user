<%@page contentType="text/html" pageEncoding="UTF-8"%>
<html>
<body>
<% 
String uid=request.getParameter("userid");
String upass=request.getParameter("password");
            
if(uid.equals("admin") && upass.equals("admin123")){
%>
<jsp:forward page="success.jsp"></jsp:forward>
<%
}else{
out.println("Invalid login id and password");
}
%>
<jsp:include page="login.html"></jsp:include>
</body>
</html>



