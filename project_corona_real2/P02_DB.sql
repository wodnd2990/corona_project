create table project_corona_3(
	p_no number(5) primary key,
	p_day date not null,
	p_name varchar2(10 char) not null,
	p_count number(5) not null
);

create sequence project_corona_3_seq;

insert into project_corona_1 values(project_corona_1_seq.nextval, to_date('2020년 3월 4일 00시','YYYY년 M월 D일 00시'),'웅재',1532);   


select * from project_corona_3;




