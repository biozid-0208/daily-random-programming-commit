class Solution {
    public int[] decode(int[] encoded, int first) {
        int len = encoded.length;
        int[] decoded = new int[len + 1];
        decoded[0] = first; 
        for(int i =0; i < len ; i++){ 
            decoded[i+1] = encoded[i] ^ decoded[i];
            
        }
        
        return decoded;
    }
}