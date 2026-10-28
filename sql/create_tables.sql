drop schema if exists weather_project cascade;
create schema weather_project;
set search_path to weather_project;

create table locations(
    location_id     int         not null,
    city            varchar(50) not null,
    country         varchar(50) not null,

    constraint pk_locations 
        primary key (location_id)
);

create table daily_weather(
    weather_id int not null,
    location_id int not null,
    weather_date DATE not null,
    temp_mean_c numeric(5,1),
    temp_max_c numeric(5,1),
    temp_min_c numeric(5,1),
    precip_mm numeric(6,2),
    rain_mm numeric(6,2),
    snowfall_cm numeric(6,2),

    constraint pk_daily_weather 
        primary key (weather_id),

    constraint fk_daily_weather_location --foreign key
        foreign key (location_id)
        references locations(location_id),

    constraint uq_location_date -- no duplicate dates allowed for the same location
        unique (location_id, date) 
);
