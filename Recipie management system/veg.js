let a = fetch("http://localhost/phpmyadmin/index.php?route=/sql&db=recipie&table=users&pos=0")
a.then((value) => {
    return value.json()
}).then((value) => {
    console.log(value)
})

