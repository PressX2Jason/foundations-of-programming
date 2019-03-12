public int interpret(int value, String[] commands, int[] args) {
    int argCount = 0;
    for(String command : commands){
      int arg = args[argCount++];
      if(command.equals("+")){
        value += arg;
      }else if(command.equals("-")){
        value -= arg;
      }else if(command.equals("*")){
        value *= arg;
      }else{
        value = -1;
        break;
      }
    }
    return value;
  }
  