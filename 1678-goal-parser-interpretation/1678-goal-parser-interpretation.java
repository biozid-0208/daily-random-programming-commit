class Solution {
    public String interpret(String command) {
        
    char[] cstr = command.toCharArray();
    StringBuilder str = new StringBuilder();
    for(int i = 0; i < command.length(); i++){
        if(cstr[i] == ')') continue;
        if(cstr[i] == '(' &&  cstr[i+1] == ')') str.append('o');
        if(cstr[i] == '(') continue;
        else str.append(cstr[i]);
    }
        return str.toString();
        
    }
}