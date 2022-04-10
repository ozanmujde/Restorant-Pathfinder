import java.util.*;
import java.io.File;  
import java.io.FileNotFoundException;  
import java.util.Scanner;
public class Main2{
    private static String[][] data_set_temp;
    private static int[][] data_set;
    private static double konumKatsayisi = 1; //-0-10 arasi, kullanıcının gireceği değerler ---- kullanıcı 0,0 noktasında başlar
    private static int konumKatsayisix = 1;
    private static int scoreKatsayisi = 1; // +
    private static int priceKatsayisix = 1; //-
    private static double priceKatsayisi = 1;

    private static int rootX = 0;
    private static int rootY = 0;
    private static int root = 0;

    private static double time = 0;
    private static double money = 0;
    private static double puan = 0;
    
    
    private static int counter = 0;
    
   
    private static Node2[] nodes;
    

    private static ArrayList<Node2> eklenenler;
    

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        System.out.println("Lütfen uzaklık, restoran puanı ve para katsayınızı giriniz !");
        konumKatsayisi = kb.nextInt();     
        scoreKatsayisi = kb.nextInt();
        priceKatsayisi = kb.nextInt();
      
        data_set_temp = new String[100][5];
        data_set = new int[100][5]; 
        nodes = new Node2[100];
        eklenenler = new ArrayList<Node2>();
        readFile();
        turnToInt();
        nodesOlustur();
        //ortalamaPara();
        findRoot();
        System.out.println("Gidilen restoranlar");
        stage_1();
        stage_1();
        stage_1();
        System.out.println();
        String sTime = ((time+(15*7))+"").substring(0,6);
        String sPara = ((time+money)+"").substring(0,6);
        System.out.println("Harcanan toplam süre: "+sTime+ " dakika");
        System.out.println("Harcanan toplam yemek parası: "+money+" lira");
        System.out.println("Gidilen restoranların toplam puanı: "+ puan);

        
                   
      
    }
     
    private static void ortalamaPara(){
        double temp = 0;
        for(int i=0; i<100; i++){   
            for(int j = 0; j<100; j++){
                if(i!=j){
                   temp += sureHesapla(nodes[i].getX(),nodes[i].getY(),nodes[j].getX(),nodes[j].getY());
                }
            }
        }
        System.out.println(temp/10000);

    }
    
    
    public static void readFile(){
        try {
            File myObj = new File("Ozan/Restorant-Pathfinder/data/restaurants.csv");
            Scanner myReader = new Scanner(myObj);
            int sayac=0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                if(sayac!=0){                
                    data_set_temp[sayac-1] = data.split(",");           
                }
                sayac++;
            }
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    }
    public static void turnToInt(){
        for(int i=0; i<data_set_temp.length; i++){
            for(int j=0; j< data_set_temp[0].length; j++){
                data_set[i][j] = Integer.parseInt(data_set_temp[i][j]);
            }
        }
    }
    
    private static double costHesapla(int x_suan, int y_suan, int x_sonraki, int y_sonraki, int score, int foodPrice){
       double mesafe = Math.sqrt(Math.pow((y_sonraki-y_suan),2) + Math.pow((x_sonraki-x_suan),2));
       return (-1*mesafe*konumKatsayisi)/53.88 + (scoreKatsayisi*score)/5.14- (foodPrice*priceKatsayisi)/33.02;

    }

    private static void nodesOlustur(){
        for(int i=0; i<100; i++){
            nodes[i] = new Node2(data_set[i][0],data_set[i][1],data_set[i][2],data_set[i][3],data_set[i][4]);
        }
    }
    private static void findRoot(){
        double max = -100;
        double temp = 0;
        for(Node2 n:nodes){
            if(!eklenenler.contains(n)){
                temp = costHesapla(rootX, rootY, n.getX(), n.getY(), n.getScore(), n.getPrice());
                if(temp > max){
                    max = temp;
                    root = n.getName();
                }
            }
        }
    }

    private static void stage_1(){
        nodes[root].setPrev(null);
        for(int i=0; i<100; i++){
            if(i != root){
                nodes[root].addChild(nodes[i]);
            }
        }
        for(int i=0; i<100; i++){
            for(int j=0; j<98; j++){
                if(i != root && i!=j && j!=root && i<nodes[root].getChildren().size()){
                    nodes[root].getChildren().get(i).addChild(nodes[j]);
                }
            }
        }

        double temp = 0;
        double temp2 = 0;
        double max2 = -1000;
        int bir = 0;
        int iki = 0;
        double sure1 = 0;
        double sure2 = 0;
        double sure =0;
        int para1 = 0;
        int para2 = 0;
        int para = 0;
        int puan1 = 0;
        int puan2 = 0;
        int temp_puan = 0;
        
        
        for(int i=0; i<100; i++){
            temp = costHesapla(rootX, rootY, nodes[i].getX(), nodes[i].getY(), nodes[i].getScore(), nodes[i].getPrice());
            sure1 = sureHesapla(rootX, rootY, nodes[i].getX(), nodes[i].getY());
            para1 = nodes[i].getPrice(); 
            puan1 = nodes[i].getScore();
            for(int j=0; j<98; j++){
                if(!eklenenler.contains(nodes[i]) && !eklenenler.contains(nodes[j]) && i != root && i!=j && j!=root && i<nodes[root].getChildren().size()){
                    temp2 = costHesapla(nodes[i].getX(), nodes[i].getY(), nodes[j].getX(), nodes[j].getY(), nodes[j].getScore(), nodes[j].getPrice());
                    sure2 = sureHesapla(nodes[i].getX(), nodes[i].getY(), nodes[j].getX(), nodes[j].getY());
                    para2 = nodes[j].getPrice();
                    puan2 = nodes[j].getScore();
                    if(temp + temp2 > max2){
                        max2 = temp + temp2;
                        bir = i;
                        iki = j;
                        sure = sure1+sure2;
                        para = para1+para2;
                        temp_puan = puan1 + puan2;
                        if(counter == 0){
                            counter++;
                            para += nodes[root].getPrice();
                            puan += nodes[root].getPrice();
                            System.out.print(root);
                        }
                    }
                }
            }
        }
        
        time += sure;
        money += para;
        puan += temp_puan;
        eklenenler.add(nodes[bir]);
        eklenenler.add(nodes[iki]);
        eklenenler.add(nodes[root]);
       // System.out.println(root+" *** "+bir+" *** "+ iki+" sure: "+sure +" para: "+para);
        System.out.print(" -> "+bir+" -> "+iki);
        root = iki;
        rootX = nodes[iki].getX();
        rootY = nodes[iki].getY();
        counter++;
        



    }
   
    private static double sureHesapla(int x_suan, int y_suan, int x_sonraki, int y_sonraki){
        double mesafe = Math.sqrt(Math.pow((y_sonraki-y_suan),2) + Math.pow((x_sonraki-x_suan),2));
        return mesafe;
    }
   
    
    
}



