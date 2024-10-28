import java.awt.*;
import javax.swing.*;
import java.util.Vector;

class biodata extends JFrame{

biodata(String s)
{
super(s);
setLayout(null);

Font f1=new Font("Times New Roman",Font.BOLD,20);

JLabel name=new JLabel("Enter your name");
JLabel email=new JLabel("Enter your email");
JLabel address=new JLabel("Enter your address");
JLabel gender=new JLabel("Select your gender");
JLabel state=new JLabel("Select your state");
JLabel hobby=new JLabel("Select your hobby");
JLabel district=new JLabel("Select your district");

name.setFont(f1);
email.setFont(f1);
address.setFont(f1);
gender.setFont(f1);
state.setFont(f1);
hobby.setFont(f1);
district.setFont(f1);

JTextField sname=new JTextField(20);
JTextField semail=new JTextField(20);
JTextArea saddress=new JTextArea(6,20);

JRadioButton male=new JRadioButton("MALE");
JRadioButton female=new JRadioButton("FEMALE");

male.setFont(f1);
female.setFont(f1);

Vector<String> v=new Vector<>();
v.add("Maharashtra");
v.add("Goa");
v.add("Karnataka");
v.add("Gujrat");

JComboBox<String> sstate=new JComboBox<>(v);
sstate.setFont(f1);

JCheckBox swimming=new JCheckBox("SWIMMING");
JCheckBox reading=new JCheckBox("READING");
JCheckBox singing=new JCheckBox("SINGING");

swimming.setFont(f1);
reading.setFont(f1);
singing.setFont(f1);

Vector<String> v1=new Vector<>();
v1.add("Sindhudurg");
v1.add("Kolhapur");
v1.add("Ratnagiri");
v1.add("Sangli");
v1.add("Satara");

JComboBox<String> sdistrict=new JComboBox<>(v1);
sdistrict.setFont(f1);

JButton submit=new JButton("SUBMIT");
JButton clear=new JButton("CLEAR");

name.setBounds(50, 30, 250, 30);
sname.setBounds(300, 30, 250, 30);
email.setBounds(50, 80, 250, 30);
semail.setBounds(300, 80, 250, 30);
address.setBounds(50, 130, 250, 30);
saddress.setBounds(300, 130, 250, 90);
gender.setBounds(50, 230, 250, 30);
male.setBounds(300, 230, 120, 30);
female.setBounds(430, 230, 120, 30);
state.setBounds(50, 280, 250, 30);
sstate.setBounds(300, 280, 250, 30);
hobby.setBounds(50, 330, 250, 30);
swimming.setBounds(300, 330, 150, 30);
reading.setBounds(450, 330, 150, 30);
singing.setBounds(600, 330, 150, 30);
district.setBounds(50, 380, 250, 30);
sdistrict.setBounds(300, 380, 250, 30);
submit.setBounds(150, 430, 120, 40);
clear.setBounds(300, 430, 120, 40);

add(name);
add(sname);
add(email);
add(semail);
add(address);
add(saddress);
add(gender);
add(male);
add(female);
add(state);
add(sstate);
add(hobby);
add(swimming);
add(reading);
add(singing);
add(district);
add(sdistrict);
add(submit);
add(clear);

setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}
}

class biodatademo{
public static void main(String args[]){
biodata b=new biodata("Student Resume");
b.setSize(800,550);
b.setVisible(true);
}
}
