import java.sql.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class jdbcswingdemo extends JFrame implements ActionListener{
JTextField t1,t2,t3,t4;
JButton add,clear;
Statement stmt;
Connection con;

jdbcswingdemo(){
FlowLayout f=new FlowLayout();
setLayout(f);
Font f1=new Font("Times New Roman",Font.BOLD,20);

JLabel l1=new JLabel("Enter your rollno");
JLabel l2=new JLabel("Enter your name");
JLabel l3=new JLabel("Enter your address");
JLabel l4=new JLabel("Enter your phone");

t1=new JTextField(10);
t2=new JTextField(10);
t3=new JTextField(10);
t4=new JTextField(10);
add=new JButton("ADD");
clear=new JButton("CLEAR");

l1.setFont(f1); l2.setFont(f1); l3.setFont(f1); l4.setFont(f1);
t1.setFont(f1); t2.setFont(f1); t3.setFont(f1); t4.setFont(f1);
add.setFont(f1); clear.setFont(f1);

JPanel p=new JPanel();
p.setSize(400,300);
p.setLayout(new GridLayout(5,2));
p.add(l1);p.add(t1);
p.add(l2);p.add(t2);
p.add(l3);p.add(t3);
p.add(l4);p.add(t4);
p.add(add);p.add(clear);
add(p);

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
setSize(600,400);
setVisible(true);

try{
Class.forName("oracle.jdbc.driver.OracleDriver");
con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE","system","manager");
System.out.println("Driver loaded successfully");
stmt=con.createStatement();
}catch(Exception e){
System.out.println("Exception found: "+e);
}

add.addActionListener(this);
clear.addActionListener(this);
}

public void actionPerformed(ActionEvent ae){
if(ae.getSource()==clear){
t1.setText("");
t2.setText("");
t3.setText("");
t4.setText("");
}else if(ae.getSource()==add){
try{
int rollno=Integer.parseInt(t1.getText());
String name=t2.getText();
String address=t3.getText();
String phone=t4.getText();

String query="insert into studinfo values("+rollno+",'"+name+"','"+address+"','"+phone+"')";
stmt.executeUpdate(query);
JOptionPane.showMessageDialog(this, "Record added successfully!");
}catch(SQLException e){
JOptionPane.showMessageDialog(this, "Record not inserted: "+e);
}
}
}

public static void main(String args[]){
new jdbcswingdemo();
}
}