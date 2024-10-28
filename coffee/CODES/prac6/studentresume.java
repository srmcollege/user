import javax.swing.*;
import java.awt.*;

class resume extends JFrame{
JTextField t1,t2,t3,t4,t5;
JButton submit,clear;

resume(String r){
super(r);
setLayout(null);
Font f1=new Font("Times New Roman",Font.BOLD,20);
Font f2=new Font("Times New Roman",Font.BOLD,15);

JLabel l1=new JLabel("Name");
JLabel l2=new JLabel("Email");
JLabel l3=new JLabel("Phone");
JLabel l4=new JLabel("Education");
JLabel l5=new JLabel("Gender");

t1=new JTextField(10);
t2=new JTextField(10);
t3=new JTextField(10);
t4=new JTextField(10);

JRadioButton male=new JRadioButton("MALE");
JRadioButton female=new JRadioButton("FEMALE");
ButtonGroup bg=new ButtonGroup();
bg.add(male);bg.add(female);

submit=new JButton("SUBMIT");
clear=new JButton("CLEAR");

submit.setFont(f1);
clear.setFont(f1);
male.setFont(f2);
female.setFont(f2);

l1.setFont(f1);
l2.setFont(f1);
l3.setFont(f1);
l4.setFont(f1);
l5.setFont(f1);


t1.setFont(f1);
t2.setFont(f1);
t3.setFont(f1);
t4.setFont(f1);

l1.setBounds(50,50,150,30);
t1.setBounds(200,50,200,30);

l2.setBounds(50,100,150,30);
t2.setBounds(200,100,200,30);

l3.setBounds(50,150,150,30);
t3.setBounds(200,150,200,30);

l4.setBounds(50,200,150,30);
t4.setBounds(200,200,200,30);

l5.setBounds(50,300,150,30);
male.setBounds(200,300,100,30);
female.setBounds(310,300,100,30);

submit.setBounds(50,350,150,40);
clear.setBounds(250,350,150,40);

add(l1);add(t1);
add(l2);add(t2);
add(l3);add(t3);
add(l4);add(t4);
add(l5);add(male);add(female);
add(submit);
add(clear);

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}
}

class studentresume{
public static void main(String args[]){
resume rs=new resume("STUDENT RESUME");
rs.setSize(600,500);
rs.setVisible(true);
}
}
