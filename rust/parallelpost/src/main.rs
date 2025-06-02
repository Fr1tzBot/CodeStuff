use std::time::Instant;
use rayon::prelude::*;
use reqwest::Client;
use scraper::Html;

pub fn parallelize<F, P, R>(func: F, params: impl IntoParallelIterator<Item = P>) -> Vec<R>
where
    F: Fn(P) -> R + Sync + Send,
    P: Send,
    R: Send,
{
    params.into_par_iter().map(func).collect()
}

/// Sends a GET request to the specified url
/// Parses the returned content into a scraper HTML object
pub async fn get(url: String) -> Html {
    println!("{url}");
    let client = Client::new();
    let result = client.get(url).send().await;
    let body = result.unwrap().text().await;
    let text = body.unwrap();
    Html::parse_document(&text)
}

pub async fn parallel_get(urls: Vec<String>) -> Vec<Html> {
    futures::future::join_all(parallelize(get, urls)).await
}


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut urls = vec![];

    for i in 1..=100 {
        urls.push(format!("https://httpbin.org/get?query={i}"))
    }

    let mut start = Instant::now();

    let results = parallel_get(urls.clone()).await;

    dbg!(results);

    println!("100 Parallel Request time: {:?}", start.elapsed());

    start = Instant::now();

    let mut output: Vec<Html> = vec![];

    for i in urls {
        output.push(get(i.to_string()).await);
    }

    println!("100 Serial Request time: {:?}", start.elapsed());

    Ok(())
}
