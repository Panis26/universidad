package taller8_cifrado;

import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class main {
	
	private Simetrico simetrico;
	private final static String ALGORITMO = "AES";

	
	public static void imprimir (byte[] contenido) {
		int i = 0;
		for (int j = 0; j < contenido.length; j++) {
			System.out.println(contenido[i]+" ");
		}
		System.out.println(contenido[i]+ " ");
	}
	
	public static void main(String[] args) throws NoSuchAlgorithmException {
		Scanner in = new Scanner(System.in);
		System.out.println("Ingrese el texto: ");
		String texto = in.nextLine(); 
		
		KeyGenerator keygen = KeyGenerator.getInstance(ALGORITMO);
		SecretKey secretKey = keygen.generateKey();
		
		
		
	}
}
