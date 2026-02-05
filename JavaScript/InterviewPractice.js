// .map((num , i , arr))
// .filter((num , i , arr))
// arr.filter((num) => num > 6)
// arr.reduce((acc , num , i , arr) => (), 0)

Array.prototype.myMap = function (cb) {
    let temp = []
    for (let i = 0; i < this.length; i++) {
        temp.push(cb(this[i], i, this))
    }

    return temp
}

Array.prototype.myFilter = function (cb) {
    let temp = []
    for (let i = 0; i < this.length; i++) {
        if (cb(this[i], i, this)) {
            temp.push(this[i])
        }
    }
    return temp
}

Array.prototype.myReduce = function (cb, initialValue) {
    let accumelator = initialValue

    for (let i = 0; i < this.length; i++) {
        accumelator = accumelator ? cb(accumelator, this[i], i, this) : this[i]
    }

    return accumelator

}




const nums = [1, 2, 3, 4]

const multiby3 = nums.myMap((num, i, arr) => {
    return num * 3
})

const greaterThan2 = nums.myFilter((num, i, arr) => {
    return num > 2
})

const sumofAll = nums.myReduce((acc, num, i, arr) => {
    return acc + num
})

console.log(multiby3)
console.log(greaterThan2)
console.log(sumofAll)