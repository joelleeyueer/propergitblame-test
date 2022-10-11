# Propergitblame installation
  Navigate to your project folder first
```bash
  $ cd project-to-test
  $ pip install propergitblame
  $ git clone [https://github.com/qwchua/propergitblame](https://github.com/qwchua/propergitblame)  
  $ cd propergitblame  
  $ pip install -e . 
  $ cd .. 
```

# Sample Usage
$ **propergitblame** -f js/game_manager.js      
$ **propergitblame** -f js/game_manager.js -n 200
$ **propergitblame** -f js/game_manager.js -n 200 -o piechart
$ **propergitblame** -f all