guests = ["Ann", "Vivienne", "Yinuo", "Grandma", "Uncle"]


guests.remove(not_attending)

guests.insert(0, "Celine")
guests.insert(2, "James")
guests.append("Erguai")

print("I can only invite two people to dinner.")
while len(guests) > 2:
    print(f"Sorry, {guests.pop()}! I can't invite you to dinner.")

for guest in guests:
    print(f"Hello, {guest}! You are still invited to dinner.")


def get_page_title(url):
    try:
        import requests
        from bs4 import BeautifulSoup
        
        # 发送GET请求获取网页内容
        response = requests.get(url)
        response.raise_for_status()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取网页标题
        title = soup.title.string if soup.title else "无标题"
        return title
    except Exception as e:
        return f"获取标题出错: {str(e)}"






















