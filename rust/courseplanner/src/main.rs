use reqwest::Error;
use scraper::{Html, Selector};

struct Constants;
impl Constants {
    pub const TERM_LIST: &'static str = "https://www.banweb.mtu.edu/owassb/bzskfcls.p_sel_crse_search";
    pub const SUBJ_LIST: &'static str = "https://www.banweb.mtu.edu/owassb/bwckgens.p_proc_term_date";
    pub const CLASS_LIST: &'static str = "https://www.banweb.mtu.edu/owassb/bzckschd.p_get_crse_unsec";
}


#[tokio::main]
async fn main() -> Result<(), Error> {

    let client = reqwest::Client::new();
    let termRes = client.get(Constants::TERM_LIST)
        .send()
        .await?;
    let body1 = termRes.text().await?;

    let document1 = Html::parse_document(&body1);

    let selector1 = Selector::parse("select[name='p_term'] > option").unwrap();

    let term_pairs: Vec<(String, String)> = document1
        .select(&selector1)
        .filter_map(|option| {
            let value = option.value().attr("value")?.to_string();
            if value.is_empty() {
                return None;
            }
            let name = option.text().collect::<Vec<_>>().join(" ").trim().to_string();
            Some((value, name))
        })
        .collect();

    let subj_data = [("p_calling_proc", "bzskfcls.P_CrseSearch"), ("p_term", "202508")];
    let subjRes = client.post(Constants::SUBJ_LIST)
        .form(&subj_data)
        .send()
        .await?;

    let body2 = subjRes.text().await?;

    let document2 = Html::parse_document(&body2);

    let selector2 = Selector::parse("select[name=sel_subj] option").unwrap();

    let subjects: Vec<(String, String)> = document2
    .select(&selector2)
    .filter_map(|element| {
        let value = element.value().attr("value")?;
        if value == "dummy" {
            return None;
        }
        let text = element.text().collect::<String>();
        Some((value.to_string(), text))
    })
    .collect();

    let class_data = [
        ("term_in", "202508"),
        ("sel_subj", "dummy"),
        ("sel_day", "dummy"),
        ("sel_schd", "dummy"),
        ("sel_insm", "dummy"),
        ("sel_camp", "dummy"),
        ("sel_levl", "dummy"),
        ("sel_sess", "dummy"),
        ("sel_instr", "dummy"),
        ("sel_ptrm", "dummy"),
        ("sel_attr", "dummy"),
        ("sel_subj", "ACC"),
        ("sel_crse", ""),
        ("sel_title", ""),
        ("sel_schd", "%"),
        ("sel_from_cred", ""),
        ("sel_to_cred", ""),
        ("sel_camp", "%"),
        ("sel_levl", "%"),
        ("sel_ptrm", "%"),
        ("sel_instr", "%"),
        ("sel_attr", "%"),
        ("begin_hh", "0"),
        ("begin_mi", "0"),
        ("begin_ap", "a"),
        ("end_hh", "0"),
        ("end_mi", "0"),
        ("end_ap", "a"),
    ];
    let classRes = client.post(Constants::CLASS_LIST)
        .form(&class_data)
        .send()
        .await?;

    let body3 = classRes.text().await?;

    let document3 = Html::parse_document(&body3);

    let selector3 = Selector::parse(

    println!("{}", body3);

    println!("Pairs: {:?}", term_pairs);
    println!("Subjects: {:?}", subjects);
    Ok(())
}
