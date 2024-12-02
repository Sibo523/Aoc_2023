use std::fs::File;
use std::io::{self, BufRead};

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
        let mut flag = true; //acsending order or not 
        let mut worked = true; // 
        
        for i in 1..parts.len() {
            if i == 1{
                if parts[i].parse::<i32>().unwrap() < parts[i-1].parse::<i32>().unwrap() {
                    flag = false;   
                }
            }
            //atoi basically
            let num = parts[i].parse::<i32>().unwrap();

            if num == parts[i-1].parse::<i32>().unwrap() {
                worked = false;
                break;
            }
            //check if all are acseding order
            if flag {
                if num < parts[i-1].parse::<i32>().unwrap() || num -3 > parts[i-1].parse::<i32>().unwrap() {
                    worked = false;
                    break;
                }
            }
            else{
                if num > parts[i-1].parse::<i32>().unwrap() || num +3 < parts[i-1].parse::<i32>().unwrap() {
                    worked = false;
                    break;
                }
            }
        }
        if worked {
            count += 1;
        }
    }
    // Print the count
    println!("{}", count);
    // Return Ok(()) to indicate success
    Ok(())
}
