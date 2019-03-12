def interpret(value, commands, args):
  for cmd, arg in zip(commands, args):
    if cmd == '+':
      value += arg
    elif cmd == '-':
      value -= arg
    elif cmd == '*':
      value *= arg
    else:
      return -1
  return value
