SELECT
  (1) AS `a`
FROM
  `my_model`
WHERE
  DATE(
    CONVERT_TZ(
      `my_model`.`my_datetime_field`,
      'UTC',
      'Europe/Paris'
    )
  ) = '2017-07-06'
LIMIT
  1;