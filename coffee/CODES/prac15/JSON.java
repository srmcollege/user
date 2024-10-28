// //JSON Encoding

//import org.json.simple.JSONObject;     
//public class JSON{     
//public static void main(String args[]){     
//JSONObject obj=new JSONObject();     
//obj.put("name","John Doe");     
//obj.put("age",new Integer(20));     
//obj.put("salary",new Double(600000));     
//System.out.print(obj);     
//}}

// //JSON Encoding using Map

//import java.util.HashMap;   
//import java.util.Map;   
//import org.json.simple.JSONValue;   
//public class JSON{     
//public static void main(String args[]){     
//Map obj=new HashMap();     
//obj.put("name","John Doe");     
//obj.put("age",new Integer(20));     
//obj.put("salary",new Double(600000));    
//String jsonText = JSONValue.toJSONString(obj);   
//System.out.print(jsonText);   
//}}

// //JSON Encoding using List

//import java.util.ArrayList;   
//import java.util.List;   
//import org.json.simple.JSONValue;   
//public class JSON{     
//public static void main(String args[]){     
//List arr = new ArrayList();   
//arr.add("John Doe");     
//arr.add(new Integer(20));     
//arr.add(new Double(600000));    
//String jsonText = JSONValue.toJSONString(arr);   
//System.out.print(jsonText);   
//}}  

// //JSON Decoding

import java.util.HashMap;   
import java.util.Map;   
import org.json.simple.JSONValue;   
public class JSON{     
public static void main(String args[]){     
Map obj=new HashMap();     
obj.put("name","John Doe");     
obj.put("age",new Integer(20));     
obj.put("salary",new Double(600000));    
String jsonText = JSONValue.toJSONString(obj);   
System.out.print(jsonText);   
}}     


