use std::vec::Vec;

fn uniq(list: Vec<i32>) -> Vec<i32> {
    let mut outtlist: Vec<i32> = Vec::new();

    for i in list {
        if !outtlist.contains(&i) {
            outtlist.push(i);
        }
    }

    outtlist
}

fn sort(list: Vec<i32>) -> Vec<i32> {
    let mut outlist = list;
    outlist.sort();
    outlist
}

fn main() {
    let mut list = vec![5,8,4,2,1,5,7,3,5,32,3,6,7,7,54,3,2,4,7,87,43,4,3,7,542];
    dbg!(&list);
    list = uniq(list);
    dbg!(&list);
    list = sort(list);
    dbg!(list);
}
