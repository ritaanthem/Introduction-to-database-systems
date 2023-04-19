drop database if exists library;
create database library;
use library;
create table Book(
  ID  char(8) PRIMARY KEY,
  name  varchar(10) NOT NULL,
  author varchar(10),
  price float,
  status int DEFAULT 0
);
create table Reader(
  ID  char(8) PRIMARY KEY,
  name  varchar(10),
  age   int,
  address varchar(20)
);
create table Borrow(
  book_ID char(8),
  Reader_ID char(8),
  Borrow_date date,
  Return_date date,
  PRIMARY KEY (book_ID,Reader_ID),
  FOREIGN KEY (book_ID) REFERENCES Book(ID),
  FOREIGN KEY (Reader_ID) REFERENCES Reader(ID)
);



# 插入书籍
insert into Book value('b1', '数据库系统实现', 'Ullman', 59.0, 0);
insert into Book value('b2', '数据库系统概念', 'Abraham', 59.0, 1);
insert into Book value('b3', 'C++ Primer', 'Stanley', 78.6, 0);
insert into Book value('b4', 'Redis设计与实现', '黄建宏', 79.0, 1);
insert into Book value('b5', '人类简史', 'Yuval', 68.00, 0);
insert into Book value('b6', '史记(公版)', '司马迁', 220.2, 1);
insert into Book value('b7', 'Oracle编程艺术', 'Thomas', 43.1, 1);
insert into Book value('b8', '分布式系统及其应用', '邵佩英', 30.0, 0);
insert into Book value('b9', 'Oracle管理', '张立杰', 51.9, 1);
insert into Book value('b10', '数理逻辑', '汪芳庭', 22.0, 0);
insert into Book value('b11', '三体', '刘慈欣', 23.0, 0);
insert into Book value('b12', 'Fun python', 'Luciano', 354.2, 1);
insert into Book value('b13', 'Learn SQL', 'Seyed', 23.0, 1);
insert into Book value('b14', 'Perl&MySQL', '徐泽平', 23.0, 1);

# 插入读者
insert into Reader value('r1', '李林', 18, '中国科学技术大学东校区');
insert into Reader value('r2', 'Rose', 22, '中国科学技术大学北校区');
insert into Reader value('r3', '罗永平', 23, '中国科学技术大学西校区');
insert into Reader value('r4', 'Nora', 26, '中国科学技术大学北校区');
insert into Reader value('r5', '汤晨', 22, '先进科学技术研究院');
insert into Reader value('r6', '李小一', 18, '中国科学技术大学东校区');
insert into Reader value('r7', '王二', 22, '中国科学技术大学北校区');
insert into Reader value('r8', '赵三', 23, '中国科学技术大学西校区');
insert into Reader value('r9', '魏四', 26, '中国科学技术大学北校区');
insert into Reader value('r10', '汤大晨', 22, '先进科学技术研究院');
insert into Reader value('r11', '李平', 18, '中国科学技术大学东校区');
insert into Reader value('r12', 'Lee', 22, '中国科学技术大学北校区');
insert into Reader value('r13', 'Jack', 23, '中国科学技术大学西校区');
insert into Reader value('r14', 'Bob', 26, '中国科学技术大学北校区');
insert into Reader value('r15', '李晓', 22, '先进科学技术研究院');
insert into Reader value('r16', '王林', 18, '中国科学技术大学东校区');
insert into Reader value('r17', 'Mike', 22, '中国科学技术大学北校区');
insert into Reader value('r18', '范维', 23, '中国科学技术大学西校区');
insert into Reader value('r19', 'David', 26, '中国科学技术大学北校区');
insert into Reader value('r20', 'Vipin', 22, '先进科学技术研究院');
insert into Reader value('r21', '林立', 18, '中国科学技术大学东校区');
insert into Reader value('r22', '张悟', 22, '中国科学技术大学北校区');
insert into Reader value('r23', '袁平', 23, '中国科学技术大学西校区');

# 插入借书
insert into Borrow value('b5','r1',  '2021-03-12', '2021-04-07');
insert into Borrow value('b6','r1',  '2021-03-08', '2021-03-19');
insert into Borrow value('b11','r1',  '2021-01-12', '2021-05-19');

insert into Borrow value('b3', 'r2', '2021-02-22', '2021-03-10');
insert into Borrow value('b9', 'r2', '2021-02-22', '2021-04-10');
insert into Borrow value('b7', 'r2', '2021-04-11', NULL);

insert into Borrow value('b1', 'r3', '2021-04-02', '2021-07-19');
insert into Borrow value('b2', 'r3', '2021-04-02', '2021-07-19');
insert into Borrow value('b4', 'r3', '2021-04-02', '2021-04-09');
insert into Borrow value('b7', 'r3', '2021-04-02', '2021-04-09');

insert into Borrow value('b6', 'r4', '2021-03-31', NULL);
insert into Borrow value('b12', 'r4', '2021-03-31', '2021-07-19');

insert into Borrow value('b4', 'r5', '2021-04-10', NULL);
insert into Borrow value('b11','r5',  '2021-08-12', '2021-09-19');

insert into Borrow value('b3', 'r6', '2021-04-10', '2022-01-01');

insert into Borrow value('b1', 'r7', '2021-08-10', '2021-12-19');

insert into Borrow value('b1', 'r8', '2022-01-10', '2022-02-19');
insert into Borrow value('b5','r8',  '2021-07-12', '2021-10-07');

insert into Borrow value('b1', 'r9', '2022-03-10', '2022-03-19');
insert into Borrow value('b2', 'r9', '2022-03-10', '2021-03-19');

insert into Borrow value('b2', 'r10', '2022-03-20', NULL);
insert into Borrow value('b5','r10',  '2021-05-12', '2021-06-07');
insert into Borrow value('b11','r10',  '2021-10-12', '2021-11-19');

insert into Borrow value('b3', 'r12', '2021-04-10', '2021-08-19');

insert into Borrow value('b3', 'r13', '2021-09-10', '2021-12-19');

insert into Borrow value('b3', 'r14', '2022-01-10', NULL);

insert into Borrow value('b9', 'r15', '2021-04-19', '2021-08-19');

insert into Borrow value('b9', 'r16', '2021-10-10', '2021-12-19');

insert into Borrow value('b9', 'r17', '2022-01-10', NULL);
insert into Borrow value('b11','r17',  '2021-12-12', '2022-01-19');

insert into Borrow value('b12', 'r18', '2021-10-10', '2021-12-19');
insert into Borrow value('b13', 'r18', '2021-10-10', '2021-12-19');

insert into Borrow value('b13', 'r19', '2022-01-10', NULL);
insert into Borrow value('b5','r19',  '2022-01-12', '2022-03-07');


insert into Borrow value('b8', 'r20', '2022-01-10', '2022-02-19');

insert into Borrow value('b14', 'r22', '2021-10-10', '2021-12-19');

insert into Borrow value('b14', 'r23', '2022-01-10', NULL);

#q1
select ID,address from Reader Where name = 'Rose';

#q2
select Book.name, Borrow.Borrow_Date from Reader, Book, Borrow 
Where Reader.ID = Borrow.Reader_ID and Book.ID = Borrow.book_ID and Reader.name = 'Rose';

#q3
select Reader.name from Reader
Where not exists (select Borrow.book_ID from Borrow Where Borrow.Reader_ID = Reader.ID);

#q4
select name, price from Book Where author = 'Ullman';

#q5
select Book.name, Book.ID from Reader, Book, Borrow 
Where Reader.ID = Borrow.Reader_ID and Book.ID = Borrow.book_ID and Reader.name = '李林'and Borrow.Return_date is null;

#q6
select Reader.name from Reader, Borrow
Where Reader.ID = Borrow.Reader_ID 
Group by Reader.ID
having COUNT(distinct Borrow.book_ID) > 3;

#q7
select Reader.name , Reader.ID from Reader
Where not exists 
(select   *  from 
(Select Borrow.book_ID from Borrow, Reader Where Borrow.Reader_ID = Reader.ID and Reader.name = '李林' ) Booklilin ,
 Borrow where Borrow.Reader_ID =  Reader.ID and Borrow.book_ID = Booklilin.book_ID );

#q8
select name, ID from Book Where name like '%MySQL%';

#q9
select bor.ID, bor.name, bor.age, bor.borrow_num 
from( select Reader.ID, Reader.name, Reader.age,COUNT(Borrow.book_ID) as borrow_num
from  Reader 
LEFT JOIN Borrow
ON Reader.ID = Borrow.Reader_ID
where EXTRACT(year FROM Borrow.Borrow_date) = '2021'
group by Reader.ID, Reader.name, Reader.age
order by borrow_num DESC) bor
limit 20;

#q10
#Drop view if exists library_view;
create view library_view as
select Reader.ID as Reader_ID , Reader.name as Reader_name, Book.ID as Book_ID, Book.name as Book_name, Borrow.Borrow_date
from  (Reader 
LEFT JOIN Borrow
ON Reader.ID = Borrow.Reader_ID)
LEFT JOIN Book
ON Borrow.book_ID = Book.ID
;


select Reader_ID, COUNT(Book_ID) from library_view 
where DATEDIFF(CURDATE(), Borrow_date) < 365
group by Reader_ID;





#三

#drop procedure if exists ChangeBookID;
delimiter //
create procedure ChangeBookID( in beforeID char(8), in afterID char(8) )
  begin
  SET FOREIGN_KEY_CHECKS = 0;
  update Book set ID = afterID where ID = beforeID;
  update Borrow set book_ID = afterID where book_ID = beforeID;
  SET FOREIGN_KEY_CHECKS = 1;
  end //



delimiter ;
call ChangeBookID('b1','bb');

select * from Book;
select * from Borrow;

call ChangeBookID('bb','b1');

#四
#drop procedure  if exists CheckBook;
delimiter //
create procedure CheckBook( out wrongnum int )
  begin
	select count(*) into wrongnum from Book
    Where (exists (select * from Borrow Where Book.ID = Borrow.book_ID and Borrow.Return_date is null) and Book.status = 0 ) or (not exists (select * from Borrow Where Book.ID = Borrow.book_ID and Borrow.Return_date is null and Borrow.Borrow_date is not null  ) and Book.status = 1 ); 
  end //

  
  delimiter ;
  call CheckBook(@wrongnum);
  select @wrongnum;


#五

#Drop Trigger if exists update_status;
Delimiter //
Create Trigger update_status after Insert on Borrow for each row
begin
	if new.Borrow_date is not null and new.Return_date is null then
		update Book set status = 1
        where new.book_ID = Book.ID;
	else 
		update Book set status = 0
        where new.book_ID = Book.ID;
	end if;
end //

Delimiter ;

#Drop Trigger if exists update_status2;
Delimiter //

Create Trigger update_status2 after Update on Borrow for each row
begin
	if new.Borrow_date is not null and new.Return_date is null then
		update Book set status = 1
        where new.book_ID = Book.ID;
	else 
		update Book set status = 0
        where new.book_ID = Book.ID;
	end if;
end //

delete from Borrow where book_ID = 'b11' and Reader_ID = 'r23';
insert into Borrow value('b11','r23',  '2022-2-12', NULL);

select * from Book;
update Borrow set Borrow.Return_date = '2022-03-19' where Borrow.book_ID = 'b11' and Borrow.Reader_ID = 'r23';

select * from Book;



