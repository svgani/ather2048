li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score = 0
flag = [0,0,0,0]

function rightAdd(){
    for (var i=0;i<4;i++){
        for (var j=2;j>-1;j--){
            if (li[i][3] != 0){
                if (li[i][j+1] == li[i][j] && li[i][j]!=0){
                    flag[3] = 1
                    li[i][j+1] *= 2
                    score += li[i][j+1]
                    li[i][j] = 0
                }
            }
        }
    }
    right()
    return
  }

function upAdd(){
    for (var j=0;j<4;j++){
        for (var i=1;i<4;i++){
            if (li[0][j] != 0){
                if (li[i-1][j] == li[i][j] && li[i][j]!=0){
                    flag[0] = 1
                    li[i-1][j] *= 2
                    score += li[i-1][j]
                    li[i][j] = 0
                }
            }
        }
    }
    up()
    return
  }

function downAdd(){
    for (var j=0;j<4;j++){
        for (var i=2;i>-1;i--){
            if (li[3][j] != 0){
                if (li[i+1][j] == li[i][j] && li[i][j]!=0){
                    flag[2] = 1
                    li[i+1][j] *= 2
                    score += li[i+1][j]
                    li[i][j] = 0
                }
            }
        }
    }
    down()
    return
  }

function leftAdd(){
    for (var i=0;i<4;i++){
        for (var j=1;j<4;j++){
            if (li[i][0] != 0){
                if (li[i][j-1] == li[i][j] && li[i][j]!=0){
                    flag[1] = 1
                    li[i][j-1] *= 2
                    score += li[i][j-1]
                    li[i][j] = 0
                }
            }
        }
    }
    left()
    return
}


const upCheck = (req,res) => {
  up()
  upAdd()
  if (flag[0]==0)
    res.render('gamePage',{
      list : li,
      score: score
    });
  else{
    fillPosition()
    res.render('gamePage',{
      list : li,
      score: score
    });
  }
}

const downCheck = (req,res) => {
  down()
  downAdd()
  if (flag[2]==0)
    res.render('gamePage',{
      list : li,
      score: score
    });
  else{
    fillPosition()
    res.render('gamePage',{
      list : li,
      score: score
    });
  }
}

const rightCheck = (req,res) => {
  right()
  rightAdd()
  if (flag[3]==0)
    res.render('gamePage',{
      list : li,
      score: score
    });
  else{
    fillPosition()
    res.render('gamePage',{
      list : li,
      score: score
    });
  }
}

const leftCheck = (req,res) => {
  left()
  leftAdd()
  if (flag[1]==0)
    res.render('gamePage',{
      list : li,
      score: score
    });
  else{
    fillPosition()
    res.render('gamePage',{
      list : li,
      score: score
    });
  }
}

function left(){
  for (var i=0;i<4;i++){
    index1 = 0
    if (li[i][0] != 0)
        index1+=1
    for (var j=1;j<4;j++)
        if (li[i][j] != 0){
            if (index1<j){
                flag[1] = 1
                li[i][index1] = li[i][j]
                li[i][j] = 0
            }
            index1+=1
        }
  }
}

function right() {
  for (var i=0;i<4;i++){
        index1 = 3
        if (li[i][3] != 0)
            index1-=1
        for (var j=2;j>-1;j--)
            if (li[i][j] != 0){
                if (index1>j){
                    flag[3] = 1
                    li[i][index1] = li[i][j]
                    li[i][j] = 0
                }
                index1-=1
            }
  }
}

function up() {
  for (var j=0;j<4;j++){
        index1 = 0
        if (li[0][j] != 0)
            index1+=1
        for (var i=1;i<4;i++)
            if (li[i][j] != 0){
                if (index1<i){
                    flag[0] = 1
                    li[index1][j] = li[i][j]
                    li[i][j] = 0
                }
                index1+=1
            }
  }
}

function down() {
  for (var j=0;j<4;j++){
        index1 = 3
        if (li[3][j] != 0)
            index1-=1
        for (var i=2;i>-1;i--)
            if (li[i][j] != 0){
                if (index1>i){
                    flag[2] = 1
                    li[index1][j] = li[i][j]
                    li[i][j] = 0
                }
                index1-=1
            }
  }
}

// function gameOver(){
//   for (var i=0;i<4;i++){
//     for (var j=0;j<4;j++){
//             if (li[i][j] == 0)
//                 return 0
//     }
//   }
//   return(checkTempAddUP() || checkTempAddDown() || checkTempAddLeft() || checkTempAddRight())
// }

function fillPosition(){
  message = ""
  flag = [0,0,0,0]
  console.log("score: "+score)
    while (1){
      var arr = [0,1,2,3];
      var arr1 = [2,4];
      r = arr[Math.floor(Math.random() * 4)];
      c = arr[Math.floor(Math.random() * 4)];
      console.log(r,c,li[r][c])
      if (li[r][c] == 0){
          // li[r][c] = random.choices([2,4], weights=(70, 30), k=1)[0]
          li[r][c] = arr1[Math.floor(Math.random() * 2)];
          break
      }
    }
  return
}

function startFunction() {
  li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  fillPosition()
  fillPosition()
  return li
}

module.exports = {
  startFunction,
  leftCheck,
  upCheck,
  downCheck,
  rightCheck
};