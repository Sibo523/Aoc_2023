use std::fs::File;
use std::io::{self, BufRead};
fn is_valid(parts: Vec<&str> )-> bool{
    let mut acs = 0;
    let mut desc = 0;
    for i in 1..parts.len() {
        //atoi basically
        let num = parts[i].parse::<i32>().unwrap();

        if num == parts[i-1].parse::<i32>().unwrap() {}
        //check if all are acseding order
       
        if num > parts[i-1].parse::<i32>().unwrap() && num - parts[i-1].parse::<i32>().unwrap() <= 3 {
            acs += 1;
        }
        if num < parts[i-1].parse::<i32>().unwrap() && parts[i-1].parse::<i32>().unwrap() - num <= 3 {
            desc += 1;
        }

    }
    let worked = acs == parts.len()-1 || desc == parts.len()-1;
    return worked;

}

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("input.txt")?;
    
    // Create a buffered reader
    let reader = io::BufReader::new(file);
    //mut is used to make the variable mutable
    let mut count = 0;  
    
    // Iterate over lines in the file
    for line in reader.lines() {
        // Unwrap the Result to get the line content
        let line = line?;
        let parts = line.split(" ").collect::<Vec<&str>>();
        //acsending order
        for i in 0..parts.len(){
            let mut copy = parts.clone();
            copy.remove(i);
            if is_valid(copy){
                count += 1;
                break;
           }

        }
    }
    // Print the count
    println!("{}", count);
    // Return Ok(()) to indicate success
    Ok(())
}