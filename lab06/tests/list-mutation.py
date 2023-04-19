test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          Nothing
          >>> lst
          [5, 6, 7, 8, 6]
          >>> lst.insert(0, 9)
          >>> lst
          [9, 5, 6, 7, 8, 6]
          >>> x = lst.pop(2)
          >>> lst
          [9, 5, 7, 8, 6]
          >>> lst.remove(x)
          >>> lst
          9a5a83015493c89b42df02f7bc04f9f8
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b == lst
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> b is lst
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> lst = [1, 2, 3]
          >>> lst.extend([4,5])
          >>> lst
          899a28e09798b624d12f99b81d4c09e9
          # locked
          >>> lst.extend([lst.append(9), lst.append(10)])
          >>> lst
          52d4e554d0f3b220231bb17f6a634b17
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
