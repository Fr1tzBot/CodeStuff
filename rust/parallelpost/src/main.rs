use std::time::Instant;

/// Sends a GET request to the specified url
/// Parses the returned content into a scraper HTML object
pub async fn get(url: &str) -> String {
    // TODO: proper non-200 response error handling, timeouts?
    let client = reqwest::Client::new();
    let result = client.get(url).send().await;
    let body = result.unwrap().text().await;
    body.unwrap()
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut urls = vec![];

    for i in 1..=100 {
        urls.push(format!("https://httpbin.org/get?query={i}"))
    }

    let mut start = Instant::now();

    // Create a client to reuse connection
    let client = reqwest::Client::new();

    // Create futures for each request
    let futures = urls.clone().into_iter().map(|url| {
        let client = client.clone();
        tokio::spawn(async move {
            let resp = client.get(url).send().await?;
            resp.text().await
        })
    });

    // Execute all futures concurrently
    let results = futures::future::join_all(futures).await;

    // Process results
    for result in results {
        match result {
            Ok(Ok(_text)) => {},
            Ok(Err(e)) => eprintln!("Request error: {}", e),
            Err(e) => eprintln!("Task error: {}", e),
        }
    }

    println!("100 Parallel Request time: {:?}", start.elapsed());

    start = Instant::now();

    let mut output: Vec<String> = vec![];

    for i in urls {
        output.push(get(&i).await);
    }

    println!("100 Serial Request time: {:?}", start.elapsed());

    Ok(())
}
