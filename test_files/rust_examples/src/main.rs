fn factorial(n:u128) -> u128 { 
    match n {
        0 | 1 => 1,
        _ => n * factorial(n-1),
    }
}

fn main() {
    let var1 = 20;
    println!("Factorial of {}: {:?}",var1,factorial(var1));
}

