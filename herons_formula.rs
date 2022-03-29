//implementation of heron's formula
fn main() {
    println!("The area of the triangle is {}",herons_formula(3.0, 4.0,5.0)); //right angle triangle
}

fn herons_formula(a: f64, b: f64, c: f64) -> f64 /* returns a float 64bit value */ {
    let s = (a + b + c) / 2.0;
    let area = (s * (s - a) * (s - b) * (s - c)).sqrt();
    
    return area; 
    // that's the float 64bit value that we return
}
